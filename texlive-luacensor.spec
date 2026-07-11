%global tl_name luacensor
%global tl_revision 71922

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.1
Release:	%{tl_revision}.1
Summary:	Securely redact sensitive information using Lua
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luacensor
License:	lppl1.3 ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luacensor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luacensor.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides simple tools for creating redacted Its tools are
useful for lawyers, workers in sensitive industries, and others who need
to easily produce both unrestricted versions of documents (for limited,
secure release) and restricted versions of documents (for general
release) Redaction is done both by hiding all characters and by slightly
varying the length of strings to prevent jigsaw identification. It also
is friendly to screen readers by adding alt-text indicating redacted
content.

