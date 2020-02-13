import salt.utils.files
from sh import net
import json


def managed(name,
            source=None,
            hash=None,
            hash_name=None,
            saltenv='base',
            engine='jinja',
            skip_verify=False,
            context=None,
            defaults=None,
            commit=True,
            **vars):

    ret = {
        'changes': {},
        'comment': '',
        'name': name,
        'result': True
    }

    sfn, _, __ = __salt__['file.get_managed'](
        name=name,
        template=engine,
        source=source,
        source_hash=hash,
        source_hash_name=hash_name,
        user=None,
        group=None,
        mode=None,
        attrs=None,
        saltenv=saltenv,
        context=context,
        defaults=defaults,
        skip_verify=skip_verify,
        **vars)

    net.abort()

    with open(sfn, 'rb') as commands:

        for line in commands.readlines():
            line = line.strip()
            line = line.decode('utf-8')

            if line.startswith('net add ') or line.startswith('net del '):
                try:
                    net(*line[4:].split(' '))
                except Exception as e:
                    ret['result'] = False
                    ret['comment'] = e.stderr

                    return ret

    changes = json.loads(str(net.pending("json")))

    if changes.get('diffs'):
        for change in changes['diffs']:
            ret['changes'][change['fromFile']] = {'diff': '\n'.join(change['content'])}

    if __opts__['test']:

        if ret['result']:
            ret['result'] = None

        net.abort()

    elif not commit:

        net.abort()

        ret['comment'] = 'Changes have not been commited'

    else:

        if changes.get('diffs'):
            ret['comment'] = str(net.commit())
        else:
            net.abort()

    salt.utils.files.remove(sfn)

    return ret
