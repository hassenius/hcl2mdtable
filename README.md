# hcl to markdown table generator

Generates a python table from hcl variables.

Useful for documenting Terraform variable files in markdown format

## Prerequisits

pip install pyhcl

## example usage

with an input like this

```hcl
variable "datacenter" { 
  description = "Data center to provision in"
  default = "ams03" 
}

variable "key_name" { 
  description = "Name or reference of SSH key to provision softlayer instances with"
}

variable "servers" {
  description = "Number of servers to provision"
}

```


Doing this `$ python hcl2mdt.py variables.tf`

will give you that 
```
| variable           | default       |required| description                            |
|--------------------|---------------|--------|----------------------------------------|
|datacenter          |ams03          |No      |Data center to provision in             |
|servers             |               |Yes     |Number of servers to provision          |
|key_name            |               |Yes     |Name or reference of SSH key to provision softlayer instances with|

```

which Github parses like this

| variable           | default       |required| description                            |
|--------------------|---------------|--------|----------------------------------------|
|datacenter          |ams03          |No      |Data center to provision in             |
|servers             |               |Yes     |Number of servers to provision          |
|key_name            |               |Yes     |Name or reference of SSH key to provision softlayer instances with|
