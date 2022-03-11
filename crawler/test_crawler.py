
import crawler_core
import sys

def main():
  url_handle_manager = crawler_core.UrlHandleManager()
  url_handle_manager.Handle()

if __name__ == '__main__':
  sys.exit(main())