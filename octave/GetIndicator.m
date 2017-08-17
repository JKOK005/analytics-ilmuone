function res = GetIndicator(conn, code)
  txt   = sprintf(" SELECT * FROM indicators WHERE \
                    code='%s' ", code);
  
  res   = pq_exec_params(conn, txt);
  res   = res.data;
end