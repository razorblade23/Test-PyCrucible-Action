import cowsay

message = """
The most remarkable thing about my mother is that for thirty years she served
the family nothing but leftovers. Lets test this.  The original meal has never been found.
Lets test the new action that uses PIP to install PyCrucible
        -- Calvin Trillin
""".strip()

print(cowsay.get_output_string("cow", message))
