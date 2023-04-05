import os

def main():
    print('Hellow from GitHub Actions!')
    token = os.environ.get("AWS_TOKEN")
    if not token:
        raise RuntimeError("AWS_TOKEN env var is not set!")
    print("All good! we found our env var!")


if __name__ == '__main__':
    main()