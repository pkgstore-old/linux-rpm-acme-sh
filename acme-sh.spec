%global d_bin                   %{_bindir}
%global release_prefix          100

Name:                           ext-app
Version:                        2.9.0
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install apps
License:                        GPLv3
Vendor:                         Package Store <https://pkgstore.github.io>
Packager:                       Kitsune Solar <kitsune.solar@gmail.com>

Source10:                       app.acme.sh

Requires:                       bash

%description
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

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m 0755 %{SOURCE10} \
  %{buildroot}%{d_bin}/app.acme.sh


%files
%{d_bin}/app.acme.sh


%changelog
* Sun Jul 04 2021 Package Store <kitsune.solar@gmail.com> - 2.9.0-100
- INIT PKG.
