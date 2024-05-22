from jinja2 import Template

html = """
{% macro func_input(name, placeholder, type='text') -%}
    <input type='{{ type }}' name='{{ name }}' placeholder='{{ placeholder }}'>
{%- endmacro %}

<p>{{ func_input('firstname', 'Имя') }}</p>
<p>{{ func_input('lastname', 'Фамилия') }}</p>
<p>{{ func_input('address', 'Адрес') }}</p>
<p>{{ func_input('phone', 'Телефон', type='tel') }}</p>
<p>{{ func_input('email', 'Почта', type='email') }}</p>
"""

tm = Template(html)
msg = tm.render()
print(msg)
