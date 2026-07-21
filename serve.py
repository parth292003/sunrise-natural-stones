import http.server
import os
import sys

class PrettyURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Extract the path without query parameters or hash anchors
        clean_path = self.path.split('?')[0].split('#')[0]
        
        # If the path is not the root, doesn't end with a slash, and doesn't match an actual file
        if clean_path != '/' and not clean_path.endswith('/') and not os.path.exists(self.translate_path(clean_path)):
            # Check if adding '.html' matches a physical file
            html_path = clean_path + '.html'
            if os.path.exists(self.translate_path(html_path)):
                # Rewrite the path to serve the html file internally
                self.path = html_path + self.path[len(clean_path):]
                
        return super().do_GET()

if __name__ == '__main__':
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
            
    print(f"Starting Sunrise local server on http://localhost:{port} (supporting pretty URLs)...")
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, PrettyURLHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
        sys.exit(0)
