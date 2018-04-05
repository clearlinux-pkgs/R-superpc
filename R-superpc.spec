#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-superpc
Version  : 1.09
Release  : 2
URL      : https://cran.r-project.org/src/contrib/superpc_1.09.tar.gz
Source0  : https://cran.r-project.org/src/contrib/superpc_1.09.tar.gz
Summary  : Supervised principal components
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
survival analsysis. Especially useful for high-dimnesional
        data, including microarray data.

%prep
%setup -q -c -n superpc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521304082

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521304082
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library superpc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library superpc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library superpc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library superpc|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/superpc/DESCRIPTION
/usr/lib64/R/library/superpc/INDEX
/usr/lib64/R/library/superpc/Meta/Rd.rds
/usr/lib64/R/library/superpc/Meta/features.rds
/usr/lib64/R/library/superpc/Meta/hsearch.rds
/usr/lib64/R/library/superpc/Meta/links.rds
/usr/lib64/R/library/superpc/Meta/nsInfo.rds
/usr/lib64/R/library/superpc/Meta/package.rds
/usr/lib64/R/library/superpc/NAMESPACE
/usr/lib64/R/library/superpc/R/superpc
/usr/lib64/R/library/superpc/R/superpc.rdb
/usr/lib64/R/library/superpc/R/superpc.rdx
/usr/lib64/R/library/superpc/help/AnIndex
/usr/lib64/R/library/superpc/help/aliases.rds
/usr/lib64/R/library/superpc/help/paths.rds
/usr/lib64/R/library/superpc/help/superpc.rdb
/usr/lib64/R/library/superpc/help/superpc.rdx
/usr/lib64/R/library/superpc/html/00Index.html
/usr/lib64/R/library/superpc/html/R.css
