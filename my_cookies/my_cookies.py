"""Retrieve leetcode cookies from Chrome with local keyring"""

import sys
import browser_cookie3


def main():
    """Print cookies."""
    cookiejar = None

    domain_name = "leetcode.com"
    if len(sys.argv) >= 2:
        if sys.argv[1] == "cn":
            domain_name = "leetcode.cn"
        else:
            domain_name = sys.argv[1]

    if not cookiejar:
        try:
            cookiejar = browser_cookie3.edge(domain_name=domain_name)
        except Exception:
            print("get cookie from Microsoft Edge failed", file=sys.stderr)
            return
    try:
        cookiejar = browser_cookie3.chrome(domain_name=domain_name)
    except Exception:
        print("get cookie from Chrome failed", file=sys.stderr)

    if not cookiejar:
        try:
            cookiejar = browser_cookie3.firefox(domain_name=domain_name)
        except Exception:
            print("get cookie from Firefox failed", file=sys.stderr)

    leetcode_cookies = list(
-        filter(lambda c: c.name in ("LEETCODE_SESSION", "csrftoken"), cookiejar)
-    )

    if len(leetcode_cookies) < 2:
        print(
            "get cookie failed, make sure you have Chrome or Firefox installed and login in LeetCode with one of them at least once."
        )
        return

    for c in leetcode_cookies:
        print(c.name, c.value)


if __name__ == "__main__":
    main()


