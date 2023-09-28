def create_spend_chart(categories):
  """Creates a bar chart of the percentage spent in each category.

  Args:
    categories: A list of Category objects.

  Returns:
    A string representing the bar chart.
  """

  # Calculate the total amount withdrawn from all of the categories.
  total_withdrawn = 0.0
  for category in categories:
    total_withdrawn += sum([item['amount'] for item in category.ledger if item['amount'] < 0])

  # Calculate the percentage spent in each category.
  category_percentages = []
  for category in categories:
    category_percentage = sum([item['amount'] for item in category.ledger if item['amount'] < 0]) / total_withdrawn * 100
    category_percentages.append(category_percentage)

  # Round the percentage spent in each category down to the nearest 10.
  for i in range(len(category_percentages)):
    category_percentages[i] = int(category_percentages[i] // 10) * 10

  # Create the bar chart.
  bar_chart = "Percentage spent by category\n"
  for i in range(100, -10, -10):
    bar_chart += f"{i:>3}% | "
    for category_percentage in category_percentages:
      if category_percentage >= i:
        bar_chart += "o"
      else:
        bar_chart += " "
    bar_chart += "\n"

  # Add a horizontal line below the bars.
  bar_chart += "    ----"

  # Add the category names below the bars.
  for i in range(len(categories)):
    bar_chart += f"\n     {categories[i].name}"

  return bar_chart
