import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2113_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2113   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2113.x'
    header.mapIndex       = 1
    header.bgm            = 33
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
        ('ED6_DT09/CH10560._CH', 'ED6_DT09/CH10560P._CP'),
        ('ED6_DT09/CH10561._CH', 'ED6_DT09/CH10561P._CP'),
        ('ED6_DT09/CH10570._CH', 'ED6_DT09/CH10570P._CP'),
        ('ED6_DT09/CH10571._CH', 'ED6_DT09/CH10571P._CP'),
        ('ED6_DT09/CH10580._CH', 'ED6_DT09/CH10580P._CP'),
        ('ED6_DT09/CH10581._CH', 'ED6_DT09/CH10581P._CP'),
        ('ED6_DT09/CH10590._CH', 'ED6_DT09/CH10590P._CP'),
        ('ED6_DT09/CH10591._CH', 'ED6_DT09/CH10591P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 1000,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -3760,
            z           = 0,
            y           = 100,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01BB,
            word_18     = 0x1354,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 3670,
            z           = 0,
            y           = -10,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01BB,
            word_18     = 0x1355,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -90,
            z           = 0,
            y           = -11260,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01BB,
            word_18     = 0x1356,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x15E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x15E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -30,
            triggerZ            = 0,
            triggerY            = -700,
            triggerRange        = 1000,
            actorX              = -50,
            actorZ              = 0,
            actorY              = 60,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x182
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x183
@scena.Code('func_01_183')
def func_01_183():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0262, 2, 0x1312)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_195',
    )

    OP_6F(0x0000, 0)

    Jump('loc_19C')

    def _loc_195(): pass

    label('loc_195')

    OP_6F(0x0000, 60)

    def _loc_19C(): pass

    label('loc_19C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x026A, 4, 0x1354)),
            Expr.Return,
        ),
        'loc_1A8',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_1A8(): pass

    label('loc_1A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x026A, 5, 0x1355)),
            Expr.Return,
        ),
        'loc_1B4',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_1B4(): pass

    label('loc_1B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x026A, 6, 0x1356)),
            Expr.Return,
        ),
        'loc_1C0',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_1C0(): pass

    label('loc_1C0')

    Return()

# id: 0x0002 offset: 0x1C1
@scena.Code('func_02_1C1')
def func_02_1C1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D6',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_1C1')

    def _loc_1D6(): pass

    label('loc_1D6')

    Return()

# id: 0x0003 offset: 0x1D7
@scena.Code('func_03_1D7')
def func_03_1D7():
    UnlockAchievement(0x02, 0x0203, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0262, 2, 0x1312)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0262, 3, 0x1313)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BB',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_022E')
    def lambda_022E():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_022E)

    @scena.Lambda('lambda_0249')
    def lambda_0249():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0249)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x000001BC, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_296'),
        (0x00000002, 'loc_2A8'),
        (0x00000001, 'loc_2B8'),
        (-1, 'loc_2BB'),
    )

    def _loc_296(): pass

    label('loc_296')

    SetScenaFlags(ScenaFlag(0x0262, 3, 0x1313))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_2BB')

    def _loc_2A8(): pass

    label('loc_2A8')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_2B8(): pass

    label('loc_2B8')

    OP_B4(0x00)

    Return()

    def _loc_2BB(): pass

    label('loc_2BB')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['苍耀石护符'], 1)"),
            Expr.Return,
        ),
        'loc_30A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['苍耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0262, 2, 0x1312))

    Jump('loc_36C')

    def _loc_30A(): pass

    label('loc_30A')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['苍耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['苍耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_36C(): pass

    label('loc_36C')

    Jump('loc_39E')

    def _loc_36F(): pass

    label('loc_36F')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_39E(): pass

    label('loc_39E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
