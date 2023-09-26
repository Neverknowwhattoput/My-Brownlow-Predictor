install.packages('fitzRoy')

library(fitzRoy)

# downloads player stats for 2023 from AFL website
stats2023 <- fetch_player_stats(2023, comp = "AFLM")
write.csv(stats2023, '../data/landing/player_stats_23_afl.csv')

matches_2023 <- fetch_fixture(season = 2023)
# drop round byes column as it is a list within a column
matches_2023 <- subset(matches_2023, select = -c(round.byes))
write.csv(matches_2023, '../data/landing/match_results_23.csv')


# downloads player stats from previous years from fryzigg data source
# this source includes brownlow votes up to 2021
stats_fry <- fetch_player_stats(season = 2012:2022, comp = "AFLM", source = "fryzigg")

write.csv(stats_fry, '../data/landing/player_stats_12-22_fry.csv')

# download historic data from footywire source as this contains the supercoach data
stats_fw <- fetch_player_stats(season = 2012:2022, 
                                               comp = "AFLM", 
                                               source = "footywire")

write.csv(stats_fw, '../data/landing/player_stats_12-22_fry.csv')

# since the fryzigg source does not currently contain brownlow votes for 2022,
# they are sourced from the footytables website
stats2022_tables <- fetch_player_stats(season=2022, comp="AFLM", source="afltables")
write.csv(stats2022_tables, '../data/landing/player_stats_22_tables.csv')

coaches_votes <- fetch_coaches_votes(season=2012:2022)
