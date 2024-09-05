.DELETE_ON_ERROR:

VOLUME = 30

PYTHON = python3

SCRIPT = lower_volume.py
ROM = x5.bin
HACK = hack.bin

$(HACK): $(SCRIPT)
	$(PYTHON) $(SCRIPT) $(VOLUME)

clean:
	rm -rf $(HACK)
