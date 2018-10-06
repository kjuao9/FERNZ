from cargo import Cargo

cargo = Cargo(id='iron_sand',
              type_name='string(STR_CARGO_NAME_IRON_SAND)',
              unit_name='string(STR_CARGO_NAME_IRON_SAND)',
              type_abbreviation='string(STR_CID_IRON_SAND)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.0',
              cargo_payment_list_colour='118',
              is_freight='1',
              cargo_classes='bitmask(CC_BULK)',
              cargo_label='ISND',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='TTD_STR_TONS',
              items_of_cargo='TTD_STR_QUANTITY_IRON_ORE',
              penalty_lowerbound='30',
              single_penalty_length='255',
              price_factor='60',
              capacity_multiplier='1',
              icon_indices=(9, 0))