# Log Report Task

An Apache-style access log is available at `/app/access.log`.

Parse the log and write a JSON summary report to `/app/report.json`.

## Required output format

The file must be valid JSON with exactly these three keys:

```json
{
  "total_requests": <integer — total number of log lines>,
  "unique_ips":     <integer — number of distinct client IP addresses>,
  "top_path":       <string  — the URL path that appears most often in GET/POST/etc. requests>
}
```

## Success criteria

1. `/app/report.json` exists and contains valid JSON.
2. `total_requests` is the correct integer count of all log entries.
3. `unique_ips` is the correct integer count of distinct IP addresses.
4. `top_path` is the string path with the highest request count.
