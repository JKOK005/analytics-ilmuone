function res = GetData(conn, c_code, i_code)
  txt = sprintf(" SELECT * FROM historical_data WHERE \
                  country_code='%s' and \
                  indicator_code='%s'; ", c_code, i_code);

  res = pq_exec_params(conn, txt);
  res = cell2mat(res.data(1,3:end));
end 