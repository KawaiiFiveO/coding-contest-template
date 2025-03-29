import jinja2

def nl2p(value):
    paragraphs = value.split("\n")
    return "".join(f"<p>{p.strip()}</p>" for p in paragraphs if p.strip())

def main():
    # Set up Jinja2 to load templates from the current directory
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    env.filters['nl2p'] = nl2p
    template = env.get_template('template.html')  # Make sure your Jinja template is named "template.html"

    # Define your contest title and sample problems data
    contest_title = "Placeholder Contest Title"
    site_title = "Coding Contest Template"
    copyright = "2025 TsunDev. All problems are fictional. Fight me."
    problems = [
        {
            "id": "A",
            "name": "Quick Maths",
            "io": "standard input/output",
            "time_limit": "1",
            "memory_limit": "256",
            "points": "100",
            "description": r"""
                Given two integers \( A \) and \( B \), print their sum.
            """,
            "input_description": r"""
                The first line contains two integers \( A \) and \( B \) \( (0 ≤ A ≤ 100, 0 ≤ B ≤ 100)\).
            """,
            "output_description": r"""
                Print the sum of \( A \) and \( B \).
            """,
            "examples": [
                {"input": "2 2", "output": "4"},
                {"input": "9 10", "output": "19"}
            ],
            "explanation": r"""
                In the first example, 2 + 2 = 4.
            """
        },
        {
            "id": "B",
            "name": "Two Sum",
            "io": "standard input/output",
            "time_limit": "2",
            "memory_limit": "512",
            "points": "150",
            "description": r"""
                You are given an array of \( n \) integers and an integer \( t \). Your task is to determine whether there exist two distinct elements in the array such that their sum equals \( t \).
                If such a pair exists, output the 1-indexed positions of any such pair. If there are multiple valid answers, output any of them. If no such pair exists, output <code>IMPOSSIBLE</code>.
            """,
            "input_description": r"""
                The first line contains two integers \( n \) and \( t \) \( (2 ≤ n ≤ 10^5, -10^9 ≤ t ≤ 10^9)\).
                The second line contains \( n \) integers \( a_1, a_2, ..., a_n \) \((-10^9 ≤ a_i ≤ 10^9)\).
            """,
            "output_description": r"""
                If there exists a pair \( (i,j) (i < j) \) such that \( a_i + a_j = t) \), output two integers representing the indices \( i \) and \( j \).
                If no such pair exists, output <code>IMPOSSIBLE</code>.
            """,
            "examples": [
                {"input": "4 9\n2 7 11 15", "output": "1 2"},
            ]
        },
    ]

    # Data dictionary to pass to the template
    data = {
        "contest_title": contest_title,
        "site_title": site_title,
        "copyright": copyright,
        "problems": problems
    }

    # Render the template with the provided data
    rendered_html = template.render(data)

    # Write the rendered HTML to a file
    with open("deploy/index.html", "w", encoding="utf-8") as f:
        f.write(rendered_html)

    print("Build complete! Check your index.html file, genius.")

if __name__ == "__main__":
    main()
