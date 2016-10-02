"""
strdl is a HTML documentation generator for python file

strdl_gen.py handles the generation of the HTML files

author: Alexander Mechler

Copyright (C) 2016 Alexander Mechler

Licenced under the MIT license
"""


def generate_file(struct):
    """
    Generates an HTML strdl documentation of the file
    :param struct: A strdl_struct to generate the HTML from
    :return: None
    """
    html = '';
    html_header = '''<p style="text-align: center;">{FILENAME}</p>
<hr />
<p style="text-align: left;">{FILE_DOC}</p>
<hr />'''

    html_function = '''<p/><table style="height: 71px; margin-left: auto; margin-right: auto; width: 100%;" border="1">
<tbody>
<tr>
<td colspan="2">
<p>{FUNCT}: {DESCRIPTION}</p>
</td>
</tr>
 <tr>
<td width="15%">&nbsp;Return</td>
<td width="85%">&nbsp;{RETURN_DOC}</td>
</tr>
<tr>
<td>&nbsp;Parameters</td>
<td>'''

    html_function_param = '''
{PARAM}: {PARAM_DOC}
'''

    html_function_close = '''
    </td>
    </tr>
</tbody>
</table>'''

    html_footer = '''<hr />
<p style="text-align: center;">Generated by strdl v0.1</p>'''

    html_header = html_header.replace('{FILENAME}', struct.filename)
    html_header = html_header.replace('{FILE_DOC}', struct.file_docs)

    html += html_header

    for function in struct.functs:
        temp_funct = html_function
        temp_funct = temp_funct.replace('{FUNCT}', function.name)
        temp_funct = temp_funct.replace('{DESCRIPTION}', function.desc)
        temp_funct = temp_funct.replace('{RETURN_DOC}', function.return_doc)
        for param in function.params:
            temp_param = html_function_param
            temp_param = temp_param.replace('{PARAM}', param.param)
            temp_param = temp_param.replace('{PARAM_DOC}', param.docs)
            temp_funct += temp_param + '<hr />'
        temp_funct += html_function_close
        html += temp_funct

    html += html_footer

    with open(struct.filename + '.html', '+w') as f:
        f.write(html)
