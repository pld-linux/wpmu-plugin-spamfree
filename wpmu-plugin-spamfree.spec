%define		package	wpmu
%define		plugin	spamfree
Summary:	WordPressMU SpamFree Anti-Spam
Name:		wpmu-plugin-%{plugin}
Version:	2.1.1.2
Release:	0.1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://downloads.wordpress.org/plugin/wp-spamfree.zip
# Source0-md5:	6bcd8e13affa6f9530758707e673fd2e
URL:		http://wordpress.org/extend/plugins/wp-spamfree/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
Requires:	wpmu >= 2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wp_root		%{_datadir}/wpmu
%define		wp_content	%{wp_root}/wp-content
%define		pluginsdir	%{wp_content}/plugins
%define		plugindir	%{pluginsdir}/%{plugin}
%define		_sysconfdir	/etc/webapps/wpmu

%description
An extremely powerful WordPress anti-spam plugin that eliminates blog
comment spam, including trackback and pingback spam. Finally, you can
enjoy a spam-free WordPress blog! Includes spam-free contact form
feature as well.

%prep
%setup -qn wp-%{plugin}
%undos readme.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{wp_content},%{pluginsdir},%{_sysconfdir}}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm $RPM_BUILD_ROOT%{plugindir}/readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{plugindir}
