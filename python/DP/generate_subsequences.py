from jinja2 import Template

nums = [1, 101, 2, 3, 100, 4, 5]

def find_increasing_subsequences(nums):
    res = []

    def backtrack(start, subSeq):
        if len(subSeq) >= 2:
            res.append(subSeq[:])

        for i in range(start, len(nums)):
            if not subSeq or nums[i] > subSeq[-1]:
                subSeq.append(nums[i])
                backtrack(i + 1, subSeq)
                subSeq.pop()

    backtrack(0, [])
    return res

subsequences = find_increasing_subsequences(nums)

# HTML template with Bootstrap
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Increasing Subsequences</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-4">
    <h2 class="mb-4">All Increasing Subsequences of {{ nums }}</h2>
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-3">
        {% for seq in subsequences %}
        <div class="col">
            <div class="card shadow-sm p-2">
                {% for num in seq %}
                    <span class="badge bg-primary me-1">{{ num }}</span>
                {% endfor %}
            </div>
        </div>
        {% endfor %}
    </div>
</div>
</body>
</html>
"""

# Render template
template = Template(html_template)
output_html = template.render(nums=nums, subsequences=subsequences)

# Save to file
with open("increasing_subsequences.html", "w") as f:
    f.write(output_html)

print("✅ HTML file generated: increasing_subsequences.html")
