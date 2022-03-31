%global d_bin                   %{_bindir}
%global release_prefix          1000

Name:                           acme-sh
Version:                        3.0.3
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install apps
License:                        GPLv3

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
* Thu Mar 31 2022 Package Store <pkgstore@mail.ru> - 3.0.3-1000
- UPD: Rebuild by Package Store.
- UPD: File "acme-sh.spec".

* Mon Mar 28 2022 Package Store <pkgstore@mail.ru> - 3.0.3-100
- NEW: Acme.SH v3.0.3.

* Sun Jul 04 2021 Package Store <pkgstore@mail.ru> - 2.9.0-100
- INIT PKG.
