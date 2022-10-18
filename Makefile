new-example:
	@read -p "Script/example Name: " project; \
	echo "Description:" && read description; \
	mkdir -p $$project/ && touch $$project/README.md && echo "## "$$project "\n\n$$description" > $$project/README.md; \
	echo 1. '`'$$project'`': $$description >> README.md; \
	echo "Created new directory for $$project"; \
