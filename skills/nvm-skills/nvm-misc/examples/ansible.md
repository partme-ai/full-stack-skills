## Instructions

Use Ansible to install nvm via the install script.

### Example

```yaml
- name: Install nvm
  ansible.builtin.shell: >
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
  args:
    creates: "{{ ansible_env.HOME }}/.nvm/nvm.sh"
```

Reference: https://github.com/nvm-sh/nvm/blob/master/README.md#ansible
