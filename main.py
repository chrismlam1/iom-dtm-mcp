"""
IOM DTM (Displacement Tracking Matrix) MCP Server
Model Context Protocol server for IOM displacement tracking data.
Provides access to displacement statistics, mobility tracking, and flow monitoring.
"""

import os
from typing import Dict
import httpx
from mcp.server.fastmcp import FastMCP
import json
import logging

# Initialize FastMCP server
mcp = FastMCP("iom_dtm")

# Constants
API_BASE_URL = 'https://dtm.iom.int/api'


async def make_request(url: str, params: Dict) -> str:
    """Make HTTP request to DTM API"""
    logging.info(f"IOM DTM Request - URL: {url}, Params: {params}")
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                url,
                params=params,
                timeout=60.0,
                follow_redirects=True
            )
            response.raise_for_status()
            logging.info("IOM DTM data retrieved successfully")
            return response.text
        except Exception as e:
            logging.error(f"IOM DTM API request failed: {e}")
            return json.dumps({"error": f"request_failed: {str(e)}"})


@mcp.tool(
    name="get_displacement_data",
    description="Get IDP (Internally Displaced Persons) data for a country"
)
async def get_displacement_data(
    country: str,
    start_date: str = "",
    end_date: str = "",
    admin_level: int = 1
) -> str:
    """
    Get displacement tracking data
    
    Args:
        country: Country name or ISO3 code
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        admin_level: Administrative level (1, 2, or 3)
    
    Returns:
        JSON string with displacement data
    """
    params = {
        "country": country,
        "start_date": start_date,
        "end_date": end_date,
        "admin": admin_level,
        "format": "json"
    }
    
    params = {k: v for k, v in params.items() if v}
    
    url = f"{API_BASE_URL}/idp-data"
    return await make_request(url, params)


@mcp.tool(
    name="get_flow_monitoring",
    description="Get migration flow monitoring data showing movement patterns"
)
async def get_flow_monitoring(
    country: str,
    flow_type: str = "all",
    start_date: str = "",
    end_date: str = ""
) -> str:
    """
    Get flow monitoring data
    
    Args:
        country: Country name or ISO3 code
        flow_type: Flow type ('arrival', 'departure', 'transit', 'all')
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
    
    Returns:
        JSON string with flow monitoring data
    """
    params = {
        "country": country,
        "flow_type": flow_type,
        "start_date": start_date,
        "end_date": end_date,
        "format": "json"
    }
    
    params = {k: v for k, v in params.items() if v}
    
    url = f"{API_BASE_URL}/flow-monitoring"
    return await make_request(url, params)


@mcp.tool(
    name="get_site_assessments",
    description="Get IDP site/camp assessments with infrastructure and services data"
)
async def get_site_assessments(
    country: str,
    site_type: str = "all",
    round_number: str = ""
) -> str:
    """
    Get site assessment data
    
    Args:
        country: Country name or ISO3 code
        site_type: Site type ('camp', 'settlement', 'host_community', 'all')
        round_number: Assessment round number
    
    Returns:
        JSON string with site assessment data
    """
    params = {
        "country": country,
        "site_type": site_type,
        "round": round_number,
        "format": "json"
    }
    
    params = {k: v for k, v in params.items() if v}
    
    url = f"{API_BASE_URL}/site-assessments"
    return await make_request(url, params)


@mcp.tool(
    name="get_baseline_assessments",
    description="Get DTM baseline assessments with comprehensive displacement data"
)
async def get_baseline_assessments(
    country: str,
    round_number: str = "",
    year: str = ""
) -> str:
    """
    Get baseline assessment data
    
    Args:
        country: Country name or ISO3 code
        round_number: Assessment round
        year: Year filter
    
    Returns:
        JSON string with baseline data
    """
    params = {
        "country": country,
        "round": round_number,
        "year": year,
        "format": "json"
    }
    
    params = {k: v for k, v in params.items() if v}
    
    url = f"{API_BASE_URL}/baseline"
    return await make_request(url, params)


@mcp.tool(
    name="get_mobility_restrictions",
    description="Get data on movement restrictions and access constraints"
)
async def get_mobility_restrictions(
    country: str,
    restriction_type: str = "all",
    start_date: str = "",
    end_date: str = ""
) -> str:
    """
    Get mobility restriction data
    
    Args:
        country: Country name or ISO3 code
        restriction_type: Type ('border', 'internal', 'curfew', 'all')
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
    
    Returns:
        JSON string with mobility restriction data
    """
    params = {
        "country": country,
        "type": restriction_type,
        "start_date": start_date,
        "end_date": end_date,
        "format": "json"
    }
    
    params = {k: v for k, v in params.items() if v}
    
    url = f"{API_BASE_URL}/mobility-restrictions"
    return await make_request(url, params)


def main():
    # Initialize and run the server
    logging.info("Starting IOM DTM MCP Server")
    mcp.run(transport='stdio')


if __name__ == "__main__":
    main()
