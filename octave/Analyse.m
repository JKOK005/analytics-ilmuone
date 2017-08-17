function res = Analyse(conn, country_code, indicator_code, start_yr)
  data  = GetData(conn, country_code, indicator_code);
  cnt   = GetCountry(conn, country_code);
  ind   = GetIndicator(conn, indicator_code);
  yrs   = [start_yr : 1 : start_yr + length(data)-1];
  
  f1    = figure();
  plot(yrs, data, 'linewidth', 1.5);
  title(sprintf("Country: %s", char(cnt(1,2))), 'fontsize', 15);
  xlabel("Years", 'fontsize', 15);
  ylabel(char(ind(1,2)), 'fontsize', 15);
end