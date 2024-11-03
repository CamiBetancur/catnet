from catnet import catnet
from pandas import read_csv, DataFrame
from pandas.testing import assert_frame_equal


def test_from_long_df():
    """Test transforming a long data frame into a Network"""
    expected_edgelist = read_csv("./tests/expected_edgelist.csv")
    expected_edgelist_with_weights = read_csv(
        "./tests/expected_edgelist_with_weights.csv")
    expected_nodelist = read_csv("./tests/expected_nodelist.csv")

    long_df = read_csv("./tests/long.csv")

    actual = catnet.from_long_df(long_df, "publication", "impact_cats")
    actual_edgelist = DataFrame(actual.edgelist)
    actual_edgelist_with_weights = DataFrame(
        actual.edgelist.with_weights())
    actual_nodelist = DataFrame(actual.nodelist)

    assert_frame_equal(expected_edgelist, actual_edgelist)
    assert_frame_equal(expected_nodelist, actual_nodelist)
    assert_frame_equal(expected_edgelist_with_weights,
                       actual_edgelist_with_weights)


def test_from_same_cell():
    """Test transforming a long data frame into a Network"""
    expected_edgelist = read_csv("./tests/expected_edgelist.csv")
    expected_edgelist_with_weights = read_csv(
        "./tests/expected_edgelist_with_weights.csv")
    expected_nodelist = read_csv("./tests/expected_nodelist.csv")

    same_cell_df = read_csv("./tests/same_cell.csv")

    actual = catnet.from_same_cell(same_cell_df,
                                   "publication",
                                   "impact_cats",
                                   sep="- ")
    actual_edgelist = DataFrame(actual.edgelist)
    actual_edgelist_with_weights = DataFrame(
        actual.edgelist.with_weights())
    actual_nodelist = DataFrame(actual.nodelist)

    assert_frame_equal(expected_edgelist, actual_edgelist)
    assert_frame_equal(expected_nodelist, actual_nodelist)
    assert_frame_equal(expected_edgelist_with_weights,
                       actual_edgelist_with_weights)
