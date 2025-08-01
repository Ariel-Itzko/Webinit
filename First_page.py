from ddgs import DDGS

module = DDGS()

query = input("Enter what you want to search: ")

results = module.text(query, max_results=5)

if not results: #משתמשים בזה ולא בביטוי השני פה בגלל שהביטוי השני בודק אם יש ערך והוא ריק גם וזה בודק אם אין בכלל תוצאות בין אם הן ריקות if results is None:
    print("No results found")
else:
  for i in results:
    print(f"Title: {i['title']}")
    print(f"Link: {i['href']}")



# עד רגע זה הקוד יכול לחפש דרך דפדפן שנקרא דאקדאקגו שהוא כאילו מאובטח יותר מגוגל ולא שומר פרטים אישיים, לפי מה שמבקשים וכותבים


# python3 -m venv venv - create a virtual environment
# source venv/bin/activate - activate the virtual environment
# pip install duckduckgo-search - install ai that can search in the internet library
# pip list - list all the libraries installed in the virtual environment
# >select interpeter - לכתוב בשורה האמצעית למעלה בשביל לבחור את הסביבה שמשתמשים בה
