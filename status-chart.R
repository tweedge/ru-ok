#!/usr/bin/Rscript

has_pkgs <- unname(installed.packages()[, 1, drop=TRUE])
needs_pkgs <- c("hrbrthemes", "ggbeeswarm", "readr", "tidyr", "dplyr", "ggplot2")

install.packages(needs_pkgs[!(needs_pkgs %in% has_pkgs)])

suppressPackageStartupMessages({
  library(hrbrthemes)
  library(ggbeeswarm)
  library(readr)
  library(tidyr)
  library(dplyr)
  library(ggplot2)
})

suppressWarnings(
  suppressMessages(
    options(readr::local_edition(1))
  )
)

args <- commandArgs(trailingOnly = TRUE)
if (length(args) == 0) {
  stop("Please supply path to directory to process", call. = FALSE)
}

fonts_dir <- system.file("fonts", "public-sans", package = "hrbrthemes")

system(
  command = sprintf("python3 export_measurements.py --input-folder %s", args[1]),
  intern = TRUE,
) -> res

read_delim(
  file = paste0(res, collapse = "\n"), 
  delim = "|", 
  col_names = c(
    "file_ts", "test", "industry", "host",
    "Site Uptime Percent Reachable World Wide", 
    "Site Uptime Percent Reachable Within Russia", 
    "Site Uptime Percent Reachable From Belarus", 
    "quip"
  ),
  col_types = "ccccdddc"
) %>% 
  mutate(
    file_ts = as.Date(substr(file_ts, 1, 10))
  ) %>% 
  select(-host, -quip) %>% 
  gather(
    measure, value, -industry, -file_ts, -test
  ) -> xdf

# Separate out tests --------------------------------------------------------------------------

xdf %>% filter(test == "HTTPS (443)") -> https
xdf %>% filter(test != "HTTPS (443)") -> http

# HTTPS ---------------------------------------------------------------------------------------

ggplot() +
  geom_violin(
    data = https,
    aes(industry, value),
    fill = NA
  ) +
  geom_quasirandom(
    data = https,
    aes(industry, value),
    groupOnX = TRUE,
    fill = "steelblue", color = "white", size = 3, shape = 21
  ) +
  scale_y_percent(limits = c(-0.05, 1.05)) +
  facet_wrap(~measure, ncol = 1, scales = "free_x") +
  labs(
    x = NULL, y = "% Uptime",
    title = "Active Uptime Measurements Of Domains Targeted by the IT ARMY of Ukraine Telegram",
    subtitle = "Chris used RIPE Atlas probes to measure target site uptime. Measurements shown in this visualization are from the HTTPS probes.\nEach dot is one website domain. Position on axis is the most recent uptime measurement.",
    caption = "Source: @_tweedge / <github.com/tweedge/ru-ok/blob/main/STATUS.md>"
  ) +
  theme_ipsum_ps(grid="Y") +
  theme(
    plot.title.position = "plot"
  ) -> gg_https

# HTTP ----------------------------------------------------------------------------------------

ggplot() +
  geom_violin(
    data = http,
    aes(industry, value),
    fill = NA
  ) +
  geom_quasirandom(
    data = http,
    aes(industry, value),
    groupOnX = TRUE,
    fill = "steelblue", color = "white", size = 3, shape = 21
  ) +
  scale_y_percent(limits = c(-0.05, 1.05)) +
  facet_wrap(~measure, ncol = 1, scales = "free_x") +
  labs(
    x = NULL, y = "% Uptime",
    title = "Active Uptime Measurements Of Domains Targeted by the IT ARMY of Ukraine Telegram",
    subtitle = "Chris used RIPE Atlas probes to measure target site uptime. Measurements shown in this visualization are from the HTTP probes.\nEach dot is one website domain. Position on axis is the most recent uptime measurement.",
    caption = "Source: @_tweedge / <github.com/tweedge/ru-ok/blob/main/STATUS.md>"
  ) +
  theme_ipsum_ps(grid="Y") +
  theme(
    plot.title.position = "plot"
  ) -> gg_http

ggsave(
  filename = "status-https.png", 
  plot = gg_https, 
  width = 1100, 
  height = 700, 
  units = "px",
  scale = 4,
  dpi = 300
)

ggsave(
  filename = "status-http.png", 
  plot = gg_http, 
  width = 1100, 
  height = 700, 
  units = "px",
  scale = 4,
  dpi = 300
)
