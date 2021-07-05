# ACME Shell script

An ACME Shell script.

- An ACME protocol client written purely in Shell (Unix shell) language.
- Full ACME protocol implementation.
- Support ACME v1 and ACME v2
- Support ACME v2 wildcard certs
- Simple, powerful and very easy to use. You only need 3 minutes to learn it.
- Bash, dash and sh compatible.
- Purely written in Shell with no dependencies on python or the official Let's Encrypt client.
- Just one script to issue, renew and install your certificates automatically.
- DOES NOT require root/sudoer access.
- Docker friendly
- IPv6 support
- Cron job notifications for renewal or error etc.

## Install

### Fedora COPR

```
$ dnf copr enable pkgstore/acme-sh
$ dnf install -y acme-sh
```

### Open Build Service (OBS)

```
# Work in Progress
```

## Update

```
$ dnf upgrade -y acme-sh
```

## Remove

```
$ dnf erase -y acme-sh
$ dnf copr remove pkgstore/acme-sh
```

## Syntax

```
$ app.acme.sh --issue -d 'example.com' -w '/home/wwwroot/example.com'
$ app.acme.sh --issue -d 'example.com' -d 'www.example.com' -d 'cp.example.com' -w '/home/wwwroot/example.com'
```
