import requests as rq
import sys

res = ""

if sys.argv[2] == 'post':
	res = rq.post(sys.argv[1])

if sys.argv[2] == 'get':
	res = rq.get(sys.argv[1])

if sys.argv[2] == 'put':
    res = rq.put(sys.argv[1])

if sys.argv[2] == 'delete':
    res = rq.delete(sys.argv[1])

if sys.argv[2] == 'patch':
    res = rq.patch(sys.argv[1])


######################################################

if sys.argv[3] == "--help":
    print("""
            request.py [url] [Method] [output]\n\n
            [Methods]
            \t get\n
            \t post\n
            \t put\n
            \t patch\n
            \t delete\n
            [outputs]
            \t--normal\n
            \t--status\n
            \t--text\n
            \t--url\n
            \t--headers\n
            \t--json\n
            \t--history\n
            \t--content\n
            \t--cookies\n
            \t--reason\n
            \t--ok\n
            \t--links\n
            \t--encoding\n
            """)
elif sys.argv[3] == '--normal':
	print(res)
elif sys.argv[3] == '--status':
	print(res.status_code)
elif sys.argv[3] == '--text':
	print(res.text)
elif sys.argv[3] == '--url':
	print(res.url)
elif sys.argv[3] == '--headers':
	print(res.headers)
elif sys.argv[3] == '--json':
	print(res.json)
elif sys.argv[3] == '--history':
	print(res.history)
elif sys.argv[3] == '--content':
	print(res.content)
elif sys.argv[3] == '--cookies':
	print(res.cookies)
elif sys.argv[3] == '--reason':
	print(res.reason)
elif sys.argv[3] == '--ok':
	print(res.ok)
elif sys.argv[3] == '--links':
	print(res.links)
elif sys.argv[3] == '--encoding':
	print(res.encoding)
