# salt-cumulus

Salt-cumulus is a small salt state, providing a easy way to configure the configuration of a cumulus switch.

It provides a simple interface to apply `net` commands from a template.

It does not provide anything else for the moment. Most of others changes can be done via usual salt states.

This is a **beta version**. Use it at your own risk!

## Installation

Simply run the following command on your switch:

`pip install salt-cumulus`

## Usage

You can use in your sls files the following state:

```
test_config:
    cumulus.managed:
      - source: salt://config
```

Assuming the config file look like:

```
net add time ntp server ch.pool.ntp.org
```

The state will parse the lines in your templated file and run each command starting with `net add` or `net del`. Others elements are ignored, so you may add comments or other data as you like, but we suggest you starts comments with `# `.

**Warning**

Running this state will abort any pending configuration first: you should avoid using the `net` command at the same time!

## Parameters

### source

Source file. Behave as the `source` argument of `file.managed`.

### hash

Hash of the file. Behave as the `hash` argument of `file.managed`.

### hash_name

Type of hash. Behave as the `hash_name` argument of `file.managed`.

### skip_verify

Skip hash verification. Behave as the `skip_verify` argument of `file.managed`.

### engine

Template format. Default to `jinja`. Behave as the `template` argument of `file.managed`.

### context

Data pased to the template. Behave as the as the `context` argument of `file.managed`.

### defaults

Default values for the context. Behave as the `defaults` argument of `file.managed`.

### commit

Commit changes when the state is applied. Default to `True`, setting it to `False` will revert changes (but will try to run them).
