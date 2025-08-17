import os

def check_mysqlserver_script(file_path="MySQLServer.py"):
    if not os.path.exists(file_path):
        return "❌ File MySQLServer.py does not exist."

    if os.path.getsize(file_path) == 0:
        return "❌ File MySQLServer.py is empty."

    with open(file_path, "r") as f:
        code = f.read()

    results = []

    # 1. Check import mysql.connector
    if "import mysql.connector" in code:
        results.append("✅ Script imports mysql.connector")
    else:
        results.append("❌ Missing 'import mysql.connector'")

    # 2. Check CREATE DATABASE
    if "CREATE DATABASE" in code.upper():
        if "ALX_BOOK_STORE" in code.upper():
            results.append("✅ Script contains CREATE DATABASE alx_book_store")
        else:
            results.append("❌ CREATE DATABASE found, but not for alx_book_store")
    else:
        results.append("❌ Missing CREATE DATABASE statement")

    # 3. Check connection code
    if "mysql.connector.connect" in code:
        results.append("✅ Script connects to MySQL server")
    else:
        results.append("❌ Missing connection to MySQL server")

    # 4. Check exception handling
    if "try" in code and "except" in code:
        results.append("✅ Script handles exceptions with try/except")
    else:
        results.append("❌ Missing exception handling (try/except)")

    # 5. Check forbidden statements (SELECT or SHOW)
    if "SELECT" in code.upper() or "SHOW" in code.upper():
        results.append("❌ Script contains forbidden SELECT/SHOW statements")
    else:
        results.append("✅ No forbidden SELECT/SHOW statements found")

    return "\n".join(results)


if __name__ == "__main__":
    print(check_mysqlserver_script("MySQLServer.py"))
