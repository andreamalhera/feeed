import pandas as pd
import pytest

from feeed.time import TimeBased as time_based


def test_time_based(mock_log_data):
    features = time_based(feature_names=['time_based']).extract(mock_log_data)
    print(features)
    assert len(features) == 76
    assert set(features.keys()) == set(['accumulated_time_min', 'accumulated_time_max',
                                        'accumulated_time_mean', 'accumulated_time_median',
                                        'accumulated_time_mode', 'accumulated_time_std',
                                        'accumulated_time_variance', 'accumulated_time_q1',
                                        'accumulated_time_q3', 'accumulated_time_iqr',
                                        'accumulated_time_geometric_mean',
                                        'accumulated_time_geometric_std',
                                        'accumulated_time_harmonic_mean',
                                        'accumulated_time_skewness', 'accumulated_time_kurtosis',
                                        'accumulated_time_coefficient_variation',
                                        'accumulated_time_entropy', 'accumulated_time_skewness_hist',
                                        'accumulated_time_kurtosis_hist', 'execution_time_min',
                                        'execution_time_max',
                                        'execution_time_mean', 'execution_time_median',
                                        'execution_time_mode', 'execution_time_std',
                                        'execution_time_variance', 'execution_time_q1',
                                        'execution_time_q3', 'execution_time_iqr',
                                        'execution_time_geometric_mean',
                                        'execution_time_geometric_std',
                                        'execution_time_harmonic_mean',
                                        'execution_time_skewness', 'execution_time_kurtosis',
                                        'execution_time_coefficient_variation',
                                        'execution_time_entropy', 'execution_time_skewness_hist',
                                        'execution_time_kurtosis_hist', 'remaining_time_min',
                                        'remaining_time_max', 'remaining_time_mean',
                                        'remaining_time_median', 'remaining_time_mode',
                                        'remaining_time_std', 'remaining_time_variance',
                                        'remaining_time_q1', 'remaining_time_q3',
                                        'remaining_time_iqr', 'remaining_time_geometric_mean',
                                        'remaining_time_geometric_std',
                                        'remaining_time_harmonic_mean', 'remaining_time_skewness',
                                        'remaining_time_kurtosis',
                                        'remaining_time_coefficient_variation',
                                        'remaining_time_entropy', 'remaining_time_skewness_hist',
                                        'remaining_time_kurtosis_hist', 'within_day_min',
                                        'within_day_max', 'within_day_mean', 'within_day_median',
                                        'within_day_mode', 'within_day_std', 'within_day_variance',
                                        'within_day_q1', 'within_day_q3', 'within_day_iqr',
                                        'within_day_geometric_mean', 'within_day_geometric_std',
                                        'within_day_harmonic_mean', 'within_day_skewness',
                                        'within_day_kurtosis', 'within_day_coefficient_variation',
                                        'within_day_entropy', 'within_day_skewness_hist',
                                        'within_day_kurtosis_hist'
                                        ])

    assert features['accumulated_time_min'] == pytest.approx(0.0, rel=1e-2)
    assert features['accumulated_time_max'] == pytest.approx(36488789.0, rel=1e-2)
    assert features['accumulated_time_mean'] == pytest.approx(396893.5456158801, rel=1e-2)
    assert features['accumulated_time_median'] == pytest.approx(11924.0, rel=1e-2)
    assert features['accumulated_time_mode'] == pytest.approx(0.0, rel=1e-2)
    assert features['accumulated_time_std'] == pytest.approx(1603193.2693230412, rel=1e-2)
    assert features['accumulated_time_variance'] == pytest.approx(2570228658802.701, rel=1e-2)
    assert features['accumulated_time_q1'] == pytest.approx(1138.5, rel=1e-2)
    assert features['accumulated_time_q3'] == pytest.approx(273793.5, rel=1e-2)
    assert features['accumulated_time_iqr'] == pytest.approx(272655.0, rel=1e-2)
    assert features['accumulated_time_geometric_mean'] == pytest.approx(10904.332835327954, rel=1e-2)
    assert features['accumulated_time_geometric_std'] == pytest.approx(44.90292804116573, rel=1e-2)
    assert features['accumulated_time_harmonic_mean'] == pytest.approx(0.0, rel=1e-2)
    assert features['accumulated_time_skewness'] == pytest.approx(11.401470845961647, rel=1e-2)
    assert features['accumulated_time_kurtosis'] == pytest.approx(172.5725804780399, rel=1e-2)
    assert features['accumulated_time_coefficient_variation'] == pytest.approx(4.039353340541942, rel=1e-2)
    assert features['accumulated_time_entropy'] == pytest.approx(7.7513093893416505, rel=1e-2)
    assert features['accumulated_time_skewness_hist'] == pytest.approx(2.6663623098416838, rel=1e-2)
    assert features['accumulated_time_kurtosis_hist'] == pytest.approx(5.1101603988544575, rel=1e-2)
    assert features['execution_time_min'] == pytest.approx(0.0, rel=1e-2)
    assert features['execution_time_max'] == pytest.approx(36051318.0, rel=1e-2)
    assert features['execution_time_mean'] == pytest.approx(169759.47397134217, rel=1e-2)
    assert features['execution_time_median'] == pytest.approx(188.0, rel=1e-2)
    assert features['execution_time_mode'] == pytest.approx(0.0, rel=1e-2)
    assert features['execution_time_std'] == pytest.approx(1442884.0333929851, rel=1e-2)
    assert features['execution_time_variance'] == pytest.approx(2081914333820.4087, rel=1e-2)
    assert features['execution_time_q1'] == pytest.approx(0.0, rel=1e-2)
    assert features['execution_time_q3'] == pytest.approx(18623.25, rel=1e-2)
    assert features['execution_time_iqr'] == pytest.approx(18623.25, rel=1e-2)
    assert features['execution_time_geometric_mean'] == pytest.approx(199.88320191111325, rel=1e-2)
    assert features['execution_time_geometric_std'] == pytest.approx(127.92792986844444, rel=1e-2)
    assert features['execution_time_harmonic_mean'] == pytest.approx(0.0, rel=1e-2)
    assert features['execution_time_skewness'] == pytest.approx(14.528527518337812, rel=1e-2)
    assert features['execution_time_kurtosis'] == pytest.approx(250.488253204707, rel=1e-2)
    assert features['execution_time_coefficient_variation'] == pytest.approx(8.499578843161146, rel=1e-2)
    assert features['execution_time_entropy'] == pytest.approx(6.221052534222753, rel=1e-2)
    assert features['execution_time_skewness_hist'] == pytest.approx(2.666603580180752, rel=1e-2)
    assert features['execution_time_kurtosis_hist'] == pytest.approx(5.110914600502133, rel=1e-2)
    assert features['remaining_time_min'] == pytest.approx(0.0, rel=1e-2)
    assert features['remaining_time_max'] == pytest.approx(36488789.0, rel=1e-2)
    assert features['remaining_time_mean'] == pytest.approx(2796232.825161036, rel=1e-2)
    assert features['remaining_time_median'] == pytest.approx(619470.0, rel=1e-2)
    assert features['remaining_time_mode'] == pytest.approx(0.0, rel=1e-2)
    assert features['remaining_time_std'] == pytest.approx(5281078.119895241, rel=1e-2)
    assert features['remaining_time_variance'] == pytest.approx(27889786108436.258, rel=1e-2)
    assert features['remaining_time_q1'] == pytest.approx(202862.5, rel=1e-2)
    assert features['remaining_time_q3'] == pytest.approx(2487420.0, rel=1e-2)
    assert features['remaining_time_iqr'] == pytest.approx(2284557.5, rel=1e-2)
    assert features['remaining_time_geometric_mean'] == pytest.approx(224736.22203397762, rel=1e-2)
    assert features['remaining_time_geometric_std'] == pytest.approx(70.1715364379747, rel=1e-2)
    assert features['remaining_time_harmonic_mean'] == pytest.approx(0.0, rel=1e-2)
    assert features['remaining_time_skewness'] == pytest.approx(3.1659682263680318, rel=1e-2)
    assert features['remaining_time_kurtosis'] == pytest.approx(11.666720436340661, rel=1e-2)
    assert features['remaining_time_coefficient_variation'] == pytest.approx(1.8886403422401359, rel=1e-2)
    assert features['remaining_time_entropy'] == pytest.approx(8.55331137332654, rel=1e-2)
    assert features['remaining_time_skewness_hist'] == pytest.approx(2.61693528788402, rel=1e-2)
    assert features['remaining_time_kurtosis_hist'] == pytest.approx(4.950830339077765, rel=1e-2)
    assert features['within_day_min'] == pytest.approx(0.0, rel=1e-2)
    assert features['within_day_max'] == pytest.approx(86390.0, rel=1e-2)
    assert features['within_day_mean'] == pytest.approx(44411.8630209018, rel=1e-2)
    assert features['within_day_median'] == pytest.approx(41160.0, rel=1e-2)
    assert features['within_day_mode'] == pytest.approx(28800.0, rel=1e-2)
    assert features['within_day_std'] == pytest.approx(20590.894075207798, rel=1e-2)
    assert features['within_day_variance'] == pytest.approx(423984918.8164276, rel=1e-2)
    assert features['within_day_q1'] == pytest.approx(28800.0, rel=1e-2)
    assert features['within_day_q3'] == pytest.approx(60433.5, rel=1e-2)
    assert features['within_day_iqr'] == pytest.approx(31633.5, rel=1e-2)
    assert features['within_day_geometric_mean'] == pytest.approx(37271.412987373165, rel=1e-2)
    assert features['within_day_geometric_std'] == pytest.approx(2.2119866614383827, rel=1e-2)
    assert features['within_day_harmonic_mean'] == pytest.approx(0.0, rel=1e-2)
    assert features['within_day_skewness'] == pytest.approx(0.18928976165276779, rel=1e-2)
    assert features['within_day_kurtosis'] == pytest.approx(-0.7723273653451699, rel=1e-2)
    assert features['within_day_coefficient_variation'] == pytest.approx(0.46325863867525635, rel=1e-2)
    assert features['within_day_entropy'] == pytest.approx(9.501009299480838, rel=1e-2)
    assert features['within_day_skewness_hist'] == pytest.approx(0.7185535544033509, rel=1e-2)
    assert features['within_day_kurtosis_hist'] == pytest.approx(0.6172758296143384, rel=1e-2)
