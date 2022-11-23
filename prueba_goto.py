from goto import with_goto

CODIGO = """
primero = 2
ultimo = 20

i = primero

label .inicio
if i == ultimo: goto .fin

print(i, end=' ')
i += 1
goto .inicio

label .fin
"""

exec(with_goto(compile(CODIGO, '', 'exec'))) # type: ignore pylint: disable=exec-used
