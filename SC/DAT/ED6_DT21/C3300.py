import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3300   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3300.x'
    header.mapIndex       = 1
    header.bgm            = 32
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
        ('ED6_DT09/CH10630._CH', 'ED6_DT09/CH10630P._CP'),
        ('ED6_DT09/CH10631._CH', 'ED6_DT09/CH10631P._CP'),
        ('ED6_DT09/CH10640._CH', 'ED6_DT09/CH10640P._CP'),
        ('ED6_DT09/CH10641._CH', 'ED6_DT09/CH10641P._CP'),
        ('ED6_DT09/CH10650._CH', 'ED6_DT09/CH10650P._CP'),
        ('ED6_DT09/CH10651._CH', 'ED6_DT09/CH10651P._CP'),
        ('ED6_DT09/CH10660._CH', 'ED6_DT09/CH10660P._CP'),
        ('ED6_DT09/CH10661._CH', 'ED6_DT09/CH10661P._CP'),
        ('ED6_DT09/CH10670._CH', 'ED6_DT09/CH10670P._CP'),
        ('ED6_DT09/CH10671._CH', 'ED6_DT09/CH10671P._CP'),
        ('ED6_DT09/CH10680._CH', 'ED6_DT09/CH10680P._CP'),
        ('ED6_DT09/CH10681._CH', 'ED6_DT09/CH10681P._CP'),
        ('ED6_DT09/CH10690._CH', 'ED6_DT09/CH10690P._CP'),
        ('ED6_DT09/CH10691._CH', 'ED6_DT09/CH10691P._CP'),
        ('ED6_DT09/CH10700._CH', 'ED6_DT09/CH10700P._CP'),
        ('ED6_DT09/CH10701._CH', 'ED6_DT09/CH10701P._CP'),
        ('ED6_DT29/CH12420._CH', 'ED6_DT29/CH12420P._CP'),
        ('ED6_DT29/CH12421._CH', 'ED6_DT29/CH12421P._CP'),
    ]

# id: 0x10001 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 93670,
            z           = -30,
            y           = -101140,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E2,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 105420,
            z           = 140,
            y           = -100870,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 75750,
            z           = -50,
            y           = -78300,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 106940,
            z           = 20,
            y           = -79600,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1AA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1AA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 39780,
            triggerZ            = -60,
            triggerY            = -82680,
            triggerRange        = 1000,
            actorX              = 39410,
            actorZ              = 1440,
            actorY              = -82290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 100900,
            triggerZ            = 60,
            triggerY            = -111450,
            triggerRange        = 1000,
            actorX              = 103740,
            actorZ              = -2060,
            actorY              = -114730,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1F2
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x1F3
@scena.Code('func_01_1F3')
def func_01_1F3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A6, 0, 0x1530)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_205',
    )

    OP_6F(0x0000, 0)

    Jump('loc_20C')

    def _loc_205(): pass

    label('loc_205')

    OP_6F(0x0000, 60)

    def _loc_20C(): pass

    label('loc_20C')

    PlaySE(461, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x212
@scena.Code('func_02_212')
def func_02_212():
    UnlockAchievement(0x02, 0x00B7, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A6, 0, 0x1530)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_286',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02A6, 0, 0x1530))

    Jump('loc_2EC')

    def _loc_286(): pass

    label('loc_286')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
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

    def _loc_2EC(): pass

    label('loc_2EC')

    Jump('loc_320')

    def _loc_2EF(): pass

    label('loc_2EF')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_320(): pass

    label('loc_320')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x32E
@scena.Code('func_03_32E')
def func_03_32E():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0366')
    def lambda_0366():
        CameraMove(101900, 20, -113230, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0366)

    @scena.Lambda('lambda_037E')
    def lambda_037E():
        OP_67(0, 8000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_037E)

    @scena.Lambda('lambda_0396')
    def lambda_0396():
        CameraSetDistance(3200, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0396)

    @scena.Lambda('lambda_03A6')
    def lambda_03A6():
        OP_6C(90000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_03A6)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42D',
    )

    OP_C0(0x0E, 0x0000001F, 0x000189C0, 0x00000032, 0xFFFE4C88, 0x0000008C, 0x000193D4, 0xFFFFFA24, 0xFFFE403A)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_43C')

    def _loc_42D(): pass

    label('loc_42D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_43C',
    )

    EventEnd(0x01)

    def _loc_43C(): pass

    label('loc_43C')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
