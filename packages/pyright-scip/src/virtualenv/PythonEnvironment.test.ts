import assert from 'assert';
import PythonEnvironment from './PythonEnvironment';
import PythonPackage from './PythonPackage';

function environment(packages: PythonPackage[]): PythonEnvironment {
    return new PythonEnvironment(new Set(), '0.1', packages);
}

test('the first package that ships a module owns it, at index 0 too', () => {
    const first = new PythonPackage('first', '1.0', ['shared/__init__.py']);
    const second = new PythonPackage('second', '2.0', ['shared/__init__.py']);
    assert.strictEqual(environment([first, second]).getPackageForModule('shared'), first);
});

test('the first package that ships a module owns it, past index 0', () => {
    const other = new PythonPackage('other', '0.1', ['other.py']);
    const first = new PythonPackage('first', '1.0', ['shared/__init__.py']);
    const second = new PythonPackage('second', '2.0', ['shared/__init__.py']);
    assert.strictEqual(environment([other, first, second]).getPackageForModule('shared'), first);
});

test('a module found at index 0 is answered from the cache', () => {
    const first = new PythonPackage('first', '1.0', ['mod.py']);
    const env = environment([first]);
    assert.strictEqual(env.getPackageForModule('mod'), first);
    first.files = [];
    assert.strictEqual(env.getPackageForModule('mod'), first);
});
