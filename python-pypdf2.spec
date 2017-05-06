%define module	PyPDF2

Summary:	Pure-Python PDF toolkit
Name:		python-pypdf2
Version:	1.26.0
Release:	1
Source0:	http://pybrary.net/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pybrary.net/pyPdf/
Provides:	%{module}
BuildRequires:	python-devel
BuildArch:	noarch

%description
A Pure-Python library built as a PDF toolkit. It is capable of:
    * extracting document information (title, author, ...),
    * splitting documents page by page,
    * merging documents page by page,
    * cropping pages,
    * merging multiple pages into a single page,
    * encrypting and decrypting PDF files.

%files
%doc README.md CHANGELOG
%{py_puresitedir}/%{module}-%{version}-py%{py_ver}.egg-info
%dir %{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --no-compile

