Name:		texlive-latex-tools-dev
Version:	64899
Release:	1
Summary:	Development pre-release of the LaTeX tools bundle
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex-tools-dev
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-tools-dev.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-tools-dev.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-tools-dev.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a pre-release version of the standard LaTeX tools
bundle. It accompanies the pre-testing kernel code
(latex-base-dev), and is intended for testing by knowledgeable
users.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/source
%doc %{_texmfdistdir}/source/latex-dev
%doc %{_texmfdistdir}/source/latex-dev/tools
%doc %{_texmfdistdir}/source/latex-dev/tools/xspace.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/xr.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/verbatim.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/varioref.ins
%doc %{_texmfdistdir}/source/latex-dev/tools/varioref.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/trace.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/tools.ins
%doc %{_texmfdistdir}/source/latex-dev/tools/theorem.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/tabularx.ins
%doc %{_texmfdistdir}/source/latex-dev/tools/tabularx.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/somedefs.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/showkeys.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/shellesc.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/rawfonts.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/multicol.ins
%doc %{_texmfdistdir}/source/latex-dev/tools/multicol.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/longtable.ins
%doc %{_texmfdistdir}/source/latex-dev/tools/longtable.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/layout.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/indentfirst.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/hhline.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/ftnright.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/fontsmpl.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/fileerr.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/enumerate.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/delarray.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/dcolumn.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/calc.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/bm.ins
%doc %{_texmfdistdir}/source/latex-dev/tools/bm.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/array.dtx
%doc %{_texmfdistdir}/source/latex-dev/tools/afterpage.ins
%doc %{_texmfdistdir}/source/latex-dev/tools/afterpage.dtx
%{_texmfdistdir}/tex
%{_texmfdistdir}/tex/latex-dev
%{_texmfdistdir}/tex/latex-dev/tools
%{_texmfdistdir}/tex/latex-dev/tools/xspace.sty
%{_texmfdistdir}/tex/latex-dev/tools/xr.sty
%{_texmfdistdir}/tex/latex-dev/tools/x.tex
%{_texmfdistdir}/tex/latex-dev/tools/verbtest.tex
%{_texmfdistdir}/tex/latex-dev/tools/verbatim.sty
%{_texmfdistdir}/tex/latex-dev/tools/varioref.sty
%{_texmfdistdir}/tex/latex-dev/tools/varioref-2016-02-16.sty
%{_texmfdistdir}/tex/latex-dev/tools/trace.sty
%{_texmfdistdir}/tex/latex-dev/tools/thp.sty
%{_texmfdistdir}/tex/latex-dev/tools/thmb.sty
%{_texmfdistdir}/tex/latex-dev/tools/thm.sty
%{_texmfdistdir}/tex/latex-dev/tools/theorem.sty
%{_texmfdistdir}/tex/latex-dev/tools/thcb.sty
%{_texmfdistdir}/tex/latex-dev/tools/thc.sty
%{_texmfdistdir}/tex/latex-dev/tools/thb.sty
%{_texmfdistdir}/tex/latex-dev/tools/tabularx.sty
%{_texmfdistdir}/tex/latex-dev/tools/somedefs.sty
%{_texmfdistdir}/tex/latex-dev/tools/showkeys.sty
%{_texmfdistdir}/tex/latex-dev/tools/showkeys-2014-10-28.sty
%{_texmfdistdir}/tex/latex-dev/tools/shellesc.sty
%{_texmfdistdir}/tex/latex-dev/tools/s.tex
%{_texmfdistdir}/tex/latex-dev/tools/rawfonts.sty
%{_texmfdistdir}/tex/latex-dev/tools/r.tex
%{_texmfdistdir}/tex/latex-dev/tools/q.tex
%{_texmfdistdir}/tex/latex-dev/tools/multicol.sty
%{_texmfdistdir}/tex/latex-dev/tools/multicol-2019-10-01.sty
%{_texmfdistdir}/tex/latex-dev/tools/multicol-2017-04-11.sty
%{_texmfdistdir}/tex/latex-dev/tools/longtable.sty
%{_texmfdistdir}/tex/latex-dev/tools/longtable-2020-01-07.sty
%{_texmfdistdir}/tex/latex-dev/tools/layout.sty
%{_texmfdistdir}/tex/latex-dev/tools/indentfirst.sty
%{_texmfdistdir}/tex/latex-dev/tools/hhline.sty
%{_texmfdistdir}/tex/latex-dev/tools/h.tex
%{_texmfdistdir}/tex/latex-dev/tools/ftnright.sty
%{_texmfdistdir}/tex/latex-dev/tools/fontsmpl.tex
%{_texmfdistdir}/tex/latex-dev/tools/fontsmpl.sty
%{_texmfdistdir}/tex/latex-dev/tools/enumerate.sty
%{_texmfdistdir}/tex/latex-dev/tools/e.tex
%{_texmfdistdir}/tex/latex-dev/tools/delarray.sty
%{_texmfdistdir}/tex/latex-dev/tools/dcolumn.sty
%{_texmfdistdir}/tex/latex-dev/tools/calc.sty
%{_texmfdistdir}/tex/latex-dev/tools/bm.sty
%{_texmfdistdir}/tex/latex-dev/tools/array.sty
%{_texmfdistdir}/tex/latex-dev/tools/array-2020-02-10.sty
%{_texmfdistdir}/tex/latex-dev/tools/array-2016-10-06.sty
%{_texmfdistdir}/tex/latex-dev/tools/afterpage.sty
%{_texmfdistdir}/tex/latex-dev/tools/.tex
%{_texmfdistdir}/doc
%doc %{_texmfdistdir}/doc/latex-dev
%doc %{_texmfdistdir}/doc/latex-dev/tools
%doc %{_texmfdistdir}/doc/latex-dev/tools/xspace.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/xr.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/verbatim.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/varioref.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/trace.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/tools-overview.tex
%doc %{_texmfdistdir}/doc/latex-dev/tools/tools-overview.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/theorem.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/tabularx.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/somedefs.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/showkeys.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/shellesc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/rawfonts.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/multicol.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/manifest.txt
%doc %{_texmfdistdir}/doc/latex-dev/tools/longtable.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/layout.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/indentfirst.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/hhline.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/ftnright.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/fontsmpl.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/fileerr.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/enumerate.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/delarray.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/dcolumn.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/changes.txt
%doc %{_texmfdistdir}/doc/latex-dev/tools/calc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/bm.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/array.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/afterpage.pdf
%doc %{_texmfdistdir}/doc/latex-dev/tools/README.md

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
