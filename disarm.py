import argparse
import requests

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Disarms the TMS machine via a server on the given port')
    parser.add_argument('port', type=int)
    args = parser.parse_args()
    
    res = requests.post('http://localhost:%d/TMS/disarm' % args.port)
    print res.status_code, res.text
    res.close()
