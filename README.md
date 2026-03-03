# IOM DTM MCP Server

Model Context Protocol (MCP) server for IOM Displacement Tracking Matrix (DTM) data.

## Features

- **Displacement Data**: IDP statistics and trends
- **Flow Monitoring**: Migration movement patterns
- **Site Assessments**: IDP camp/settlement infrastructure
- **Baseline Assessments**: Comprehensive displacement data
- **Mobility Restrictions**: Movement constraint tracking

## Installation

```bash
pip install -e .
```

## Usage

### As MCP Server

```bash
python main.py
```

### In Cloudera Agent Studio

```json
{
  "name": "iom-dtm-mcp-server",
  "type": "PYTHON",
  "args": ["--from", "path/to/iom-dtm-mcp", "run-server"],
  "env_names": []
}
```

## Tools Available

### get_displacement_data
Get IDP statistics for a country and time period.

**Parameters:**
- `country` (str): Country name or ISO3 code
- `start_date` (str): Start date (YYYY-MM-DD)
- `end_date` (str): End date (YYYY-MM-DD)
- `admin_level` (int): Administrative level (1-3)

### get_flow_monitoring
Get migration flow data showing arrival, departure, transit patterns.

### get_site_assessments
Get IDP site/camp assessments with infrastructure data.

### get_baseline_assessments
Get comprehensive DTM baseline assessment data.

### get_mobility_restrictions
Get movement restriction and access constraint data.

## Example

```python
# Get displacement data for Sudan
result = await get_displacement_data(
    country="Sudan",
    start_date="2024-01-01",
    end_date="2024-12-31",
    admin_level=2
)
```

## Data Source

IOM Displacement Tracking Matrix: https://dtm.iom.int/
