# Extract Just Bangs Searches

This tool extracts search terms from Firefox `places.sqlite` entries for the `https://bangs.tristanhavelick.com/` service.

You can usually find your Firefox `places.sqlite` database in your profile directory. For example:
- On Linux: `~/.mozilla/firefox/<profile>/places.sqlite`
- On macOS: `~/Library/Application Support/Firefox/Profiles/<profile>/places.sqlite`
- On Windows: `%APPDATA%\Mozilla\Firefox\Profiles\<profile>\places.sqlite`

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

## Sample Output

### Raw

```bash
$ ./extract_just_bangs_searches.py ~/tmp/places.sqlite

wikipedia
last of us w!
last of Us imdb!
```

### Advanced Example

```bash
$ ./extract_just_bangs_searches.py ~/tmp/places.sqlite --omit-bangs --lowercase | sort | uniq -c | sort -r | less
```
