from cargo import Cargo

cargo = Cargo(id='electrical_machines',
              type_name='string(STR_CARGO_NAME_ELECTRICAL_MACHINES)',
              unit_name='string(STR_CARGO_NAME_ELECTRICAL_MACHINES)',
              type_abbreviation='string(STR_CID_ELECTRICAL_MACHINES)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.0',
              cargo_payment_list_colour='205',
              is_freight='1',
              cargo_classes='bitmask(CC_PIECE_GOODS)',
              cargo_label='POWR',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='84',
              items_of_cargo='string(STR_CARGO_UNIT_ELECTRICAL_MACHINES)',
              penalty_lowerbound='7',
              single_penalty_length='255',
              price_factor='172',
              capacity_multiplier='1',
              icon_indices=(5, 4))
