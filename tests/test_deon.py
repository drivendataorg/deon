import pytest
import json

import deon

def test_output(checklist, tmpdir, test_format_configs):
    for frmt, fpath, known_good in test_format_configs:
        temp_file_path = tmpdir.join(fpath)
        result = deon.create(checklist, None, temp_file_path, False, False)

        if frmt != 'jupyter':
            assert temp_file_path.read() == known_good
        else:
            with open(temp_file_path, 'r') as f:
                nbdata = json.load(f)
            assert nbdata['cells'][0] == known_good

    unsupported_output = tmpdir.join('test.doc')
    with pytest.raises(deon.ExtensionException):
        deon.create(checklist, None, unsupported_output, False, False)
