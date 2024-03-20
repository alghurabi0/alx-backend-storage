-- creating a procedure in mysql
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN u_i INT)
BEGIN
  DECLARE result DECIMAL(8,2) DEFAULT 0.0;
  SELECT AVG(score) INTO result
  FROM corrections
  WHERE user_id = u_i;
  UPDATE users SET average_score = result WHERE id = u_i;
END
$$
