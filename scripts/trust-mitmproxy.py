from pathlib import Path

import certifi

mitmproxy_cert_path = Path.home() / ".mitmproxy" / "mitmproxy-ca-cert.cer"
mitmproxy_cert_path = mitmproxy_cert_path.resolve()
if mitmproxy_cert_path.is_file():
    mitmproxy_cert = mitmproxy_cert_path.read_text()
else:
    raise Exception("cannot find mitmproxy certificate!")

certifi_certs_path = Path(certifi.where()).resolve()
certifi_certs = certifi_certs_path.read_text()
if mitmproxy_cert in certifi_certs_path:
    print("mitmproxy is already trusted, no action required.")
else:
    print("mitmproxy is not trusted, adding it to certifi...")
    certifi_certs += "\n" + mitmproxy_cert
    certifi_certs_path.write_text(certifi_certs)
    print("mitmproxy is now trusted!")
