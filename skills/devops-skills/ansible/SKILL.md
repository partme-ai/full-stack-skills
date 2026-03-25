---
name: ansible
description: "Provides comprehensive guidance for Ansible automation including playbooks, roles, inventory, and module usage. Use when the user asks about Ansible, needs to automate IT tasks, create Ansible playbooks, or manage infrastructure with Ansible."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write Ansible playbooks, roles, or inventory files
- Execute ad-hoc commands or run playbooks against hosts
- Use modules (package, copy, template, service, user, etc.) for configuration and deployment
- Handle variables, conditionals, loops, and error handling in Ansible
- Set up Ansible Vault for secrets management

## How to use this skill

### Workflow

1. **Define inventory** — list target hosts in INI or YAML format
2. **Write playbook** — define hosts, tasks, handlers, and vars in YAML
3. **Organize with roles** — extract reusable tasks, templates, and defaults into roles
4. **Run and validate** — execute with `ansible-playbook` and verify idempotency

### Quick Start Example

```yaml
# site.yml
---
- name: Deploy web application
  hosts: webservers
  become: true
  vars:
    app_port: 8080
  tasks:
    - name: Install nginx
      ansible.builtin.package:
        name: nginx
        state: present

    - name: Deploy config from template
      ansible.builtin.template:
        src: templates/nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: restart nginx

  handlers:
    - name: restart nginx
      ansible.builtin.service:
        name: nginx
        state: restarted
```

```bash
# Run the playbook
ansible-playbook -i inventory/production site.yml

# Ad-hoc ping all hosts
ansible -m ping all
```

### Key Commands

| Command | Purpose |
|---------|---------|
| `ansible-playbook playbook.yml` | Run a playbook |
| `ansible -m ping all` | Test connectivity |
| `ansible-vault encrypt vars/secrets.yml` | Encrypt sensitive data |
| `ansible-galaxy init myrole` | Scaffold a new role |

## Best Practices

- Organize with roles and `group_vars/host_vars` hierarchy; avoid monolithic playbooks
- Encrypt sensitive data with `ansible-vault`; use idempotent tasks with `state` and conditionals
- Define explicit failure handling (`ignore_errors`, `block/rescue`); use tags for selective runs
- Control node requires Python; target hosts need SSH access; optionally use AWX/Tower for scheduling

## Troubleshooting

- **Connection refused**: Verify SSH keys and `ansible_user` in inventory
- **Module not found**: Check Ansible version and use FQCN (e.g., `ansible.builtin.copy`)
- **Idempotency failures**: Ensure tasks use `state` parameter and avoid shell commands where modules exist

## Keywords

ansible, playbook, role, inventory, automation, configuration management, ansible-vault, infrastructure
