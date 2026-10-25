student = {"name": "Gourav", "age": 25}

print(student.get("name"))
student.get("name")          # Key मौजूद है → उसकी value
student.get("city")          # Key नहीं है → None
student.get("city", "Sambhal")  # Key नहीं है → Sambhal
