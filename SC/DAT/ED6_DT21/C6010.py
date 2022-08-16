import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C6010_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C6010   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C6010.x'
    header.mapIndex       = 1
    header.bgm            = 62
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_B6',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_02_1CC)

    def _loc_B6(): pass

    label('loc_B6')

    Return()

# id: 0x0001 offset: 0xB7
@scena.Code('func_01_B7')
def func_01_B7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 0, 0x2210)),
            Expr.Return,
        ),
        'loc_F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 5, 0x2215)),
            Expr.Return,
        ),
        'loc_D1',
    )

    OP_B1('C6010_1')

    Jump('loc_F4')

    def _loc_D1(): pass

    label('loc_D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 6, 0x2216)),
            Expr.Return,
        ),
        'loc_E4',
    )

    OP_B1('C6010_1')

    Jump('loc_F4')

    def _loc_E4(): pass

    label('loc_E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 7, 0x2217)),
            Expr.Return,
        ),
        'loc_F4',
    )

    OP_B1('C6010_4')

    def _loc_F4(): pass

    label('loc_F4')

    Jump('loc_1B4')

    def _loc_F7(): pass

    label('loc_F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 1, 0x2211)),
            Expr.Return,
        ),
        'loc_137',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 4, 0x2214)),
            Expr.Return,
        ),
        'loc_111',
    )

    OP_B1('C6010_1')

    Jump('loc_134')

    def _loc_111(): pass

    label('loc_111')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 6, 0x2216)),
            Expr.Return,
        ),
        'loc_124',
    )

    OP_B1('C6010_2')

    Jump('loc_134')

    def _loc_124(): pass

    label('loc_124')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 7, 0x2217)),
            Expr.Return,
        ),
        'loc_134',
    )

    OP_B1('C6010_2')

    def _loc_134(): pass

    label('loc_134')

    Jump('loc_1B4')

    def _loc_137(): pass

    label('loc_137')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 2, 0x2212)),
            Expr.Return,
        ),
        'loc_177',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 4, 0x2214)),
            Expr.Return,
        ),
        'loc_151',
    )

    OP_B1('C6010_3')

    Jump('loc_174')

    def _loc_151(): pass

    label('loc_151')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 5, 0x2215)),
            Expr.Return,
        ),
        'loc_164',
    )

    OP_B1('C6010_2')

    Jump('loc_174')

    def _loc_164(): pass

    label('loc_164')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 7, 0x2217)),
            Expr.Return,
        ),
        'loc_174',
    )

    OP_B1('C6010_3')

    def _loc_174(): pass

    label('loc_174')

    Jump('loc_1B4')

    def _loc_177(): pass

    label('loc_177')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 3, 0x2213)),
            Expr.Return,
        ),
        'loc_1B4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 4, 0x2214)),
            Expr.Return,
        ),
        'loc_191',
    )

    OP_B1('C6010_4')

    Jump('loc_1B4')

    def _loc_191(): pass

    label('loc_191')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 5, 0x2215)),
            Expr.Return,
        ),
        'loc_1A4',
    )

    OP_B1('C6010_4')

    Jump('loc_1B4')

    def _loc_1A4(): pass

    label('loc_1A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 6, 0x2216)),
            Expr.Return,
        ),
        'loc_1B4',
    )

    OP_B1('C6010_3')

    def _loc_1B4(): pass

    label('loc_1B4')

    PlaySE(318, 0x00, 0x64)
    PlaySE(451, 0x01, 0x64)
    OP_12(0x000124F8, 0x000493E0, 0x00000000)

    Return()

# id: 0x0002 offset: 0x1CC
@scena.Code('func_02_1CC')
def func_02_1CC():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 0, 0x2210)),
            Expr.Return,
        ),
        'loc_319',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 5, 0x2215)),
            Expr.Return,
        ),
        'loc_241',
    )

    CameraMove(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_76(0x0001, 0x00000000, 0x0001, 25, 0, 0, 0x00, 0x00)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 300)

    Jump('loc_316')

    def _loc_241(): pass

    label('loc_241')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 6, 0x2216)),
            Expr.Return,
        ),
        'loc_2AD',
    )

    CameraMove(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_76(0x0001, 0x00000000, 0x0001, 25, 0, 0, 0x00, 0x00)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 300)

    Jump('loc_316')

    def _loc_2AD(): pass

    label('loc_2AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 7, 0x2217)),
            Expr.Return,
        ),
        'loc_316',
    )

    CameraMove(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_76(0x0001, 0x00000000, 0x0001, 25, 0, 0, 0x00, 0x00)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 300)

    def _loc_316(): pass

    label('loc_316')

    Jump('loc_6F7')

    def _loc_319(): pass

    label('loc_319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 1, 0x2211)),
            Expr.Return,
        ),
        'loc_464',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 4, 0x2214)),
            Expr.Return,
        ),
        'loc_38C',
    )

    CameraMove(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_76(0x0001, 0x00000000, 0x0001, -25, 0, 0, 0x00, 0x00)
    OP_6F(0x0000, 300)
    OP_70(0x0000, 0)

    Jump('loc_461')

    def _loc_38C(): pass

    label('loc_38C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 6, 0x2216)),
            Expr.Return,
        ),
        'loc_3F8',
    )

    CameraMove(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_76(0x0001, 0x00000000, 0x0001, 25, 0, 0, 0x00, 0x00)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 300)

    Jump('loc_461')

    def _loc_3F8(): pass

    label('loc_3F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 7, 0x2217)),
            Expr.Return,
        ),
        'loc_461',
    )

    CameraMove(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_76(0x0001, 0x00000000, 0x0001, 25, 0, 0, 0x00, 0x00)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 300)

    def _loc_461(): pass

    label('loc_461')

    Jump('loc_6F7')

    def _loc_464(): pass

    label('loc_464')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 2, 0x2212)),
            Expr.Return,
        ),
        'loc_5AF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 4, 0x2214)),
            Expr.Return,
        ),
        'loc_4D7',
    )

    CameraMove(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_76(0x0001, 0x00000000, 0x0001, -25, 0, 0, 0x00, 0x00)
    OP_6F(0x0000, 300)
    OP_70(0x0000, 0)

    Jump('loc_5AC')

    def _loc_4D7(): pass

    label('loc_4D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 5, 0x2215)),
            Expr.Return,
        ),
        'loc_543',
    )

    CameraMove(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_76(0x0001, 0x00000000, 0x0001, -25, 0, 0, 0x00, 0x00)
    OP_6F(0x0000, 300)
    OP_70(0x0000, 0)

    Jump('loc_5AC')

    def _loc_543(): pass

    label('loc_543')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 7, 0x2217)),
            Expr.Return,
        ),
        'loc_5AC',
    )

    CameraMove(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_76(0x0001, 0x00000000, 0x0001, -25, 0, 0, 0x00, 0x00)
    OP_6F(0x0000, 300)
    OP_70(0x0000, 0)

    def _loc_5AC(): pass

    label('loc_5AC')

    Jump('loc_6F7')

    def _loc_5AF(): pass

    label('loc_5AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 3, 0x2213)),
            Expr.Return,
        ),
        'loc_6F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 4, 0x2214)),
            Expr.Return,
        ),
        'loc_622',
    )

    CameraMove(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_76(0x0001, 0x00000000, 0x0001, -25, 0, 0, 0x00, 0x00)
    OP_6F(0x0000, 300)
    OP_70(0x0000, 0)

    Jump('loc_6F7')

    def _loc_622(): pass

    label('loc_622')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 5, 0x2215)),
            Expr.Return,
        ),
        'loc_68E',
    )

    CameraMove(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_76(0x0001, 0x00000000, 0x0001, -25, 0, 0, 0x00, 0x00)
    OP_6F(0x0000, 300)
    OP_70(0x0000, 0)

    Jump('loc_6F7')

    def _loc_68E(): pass

    label('loc_68E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 6, 0x2216)),
            Expr.Return,
        ),
        'loc_6F7',
    )

    CameraMove(1000, 0, -360, 0)
    OP_67(0, 2300, -10000, 0)
    CameraSetDistance(6250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_76(0x0001, 0x00000000, 0x0001, 25, 0, 0, 0x00, 0x00)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 300)

    def _loc_6F7(): pass

    label('loc_6F7')

    @scena.Lambda('lambda_06FD')
    def lambda_06FD():
        CameraSetDistance(8570, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_06FD)

    @scena.Lambda('lambda_070D')
    def lambda_070D():
        OP_67(0, 3300, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_070D)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0002)
    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x00100000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 4, 0x2214)),
            Expr.Return,
        ),
        'loc_757',
    )

    ClearScenaFlags(ScenaFlag(0x0442, 4, 0x2214))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C6000._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_79F')

    def _loc_757(): pass

    label('loc_757')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 5, 0x2215)),
            Expr.Return,
        ),
        'loc_770',
    )

    ClearScenaFlags(ScenaFlag(0x0442, 5, 0x2215))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6001._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_79F')

    def _loc_770(): pass

    label('loc_770')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 6, 0x2216)),
            Expr.Return,
        ),
        'loc_789',
    )

    ClearScenaFlags(ScenaFlag(0x0442, 6, 0x2216))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6002._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_79F')

    def _loc_789(): pass

    label('loc_789')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 7, 0x2217)),
            Expr.Return,
        ),
        'loc_79F',
    )

    ClearScenaFlags(ScenaFlag(0x0442, 7, 0x2217))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6003._SN', 101, 0, 0)
    IdleLoop()

    def _loc_79F(): pass

    label('loc_79F')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
