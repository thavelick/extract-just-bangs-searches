# Extract Just Bangs Searches

This tool extracts search terms from Firefox `places.sqlite` entries for the `https://bangs.tristanhavelick.com/` service.

## Usage

```bash
./extract_just_bangs_searches.py <db_path> [--omit-bangs] [--lowercase]
```

- `<db_path>`: Path to your Firefox `places.sqlite` database.
- `--omit-bangs`: Remove any bangs (`!`) from the search terms.
- `--lowercase`: Convert all output to lowercase.

## Example

```bash
./extract_just_bangs_searches.py ~/tmp/places.sqlite --omit-bangs --lowercase | sort | uniq -c | sort -r | less
```
