%define device otterx
%define vendor amazon

%define vendor_pretty Amazon
%define device_pretty Kindle Fire

%define installable_zip 1

%define straggler_files \
/charger_otterx\
%{nil}

%include rpm/dhd/droid-hal-device.inc
