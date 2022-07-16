import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, '玛诺利亚村方向'),
    TXT(0x03, '古罗尼山道方向'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2100.x'
    header.mapIndex       = 100
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x834
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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
            word_3A         = 100,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10161P._CP'),
        ('ED6_DT09/CH10450._CH', 'ED6_DT09/CH10450P._CP'),
        ('ED6_DT09/CH10451._CH', 'ED6_DT09/CH10451P._CP'),
        ('ED6_DT09/CH10220._CH', 'ED6_DT09/CH10220P._CP'),
        ('ED6_DT09/CH10221._CH', 'ED6_DT09/CH10221P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -18570,
            z                   = -2000,
            y                   = -37710,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 100500,
            z                   = -2070,
            y                   = 132300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 26400,
            z           = -2050,
            y           = 109110,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x016D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 22850,
            z           = -2020,
            y           = 80880,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x016D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 24710,
            z           = -2070,
            y           = 44250,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x016D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 16680,
            z           = -2060,
            y           = 9800,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x016D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1AA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1AA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 35120,
            triggerZ            = -1980,
            triggerY            = 46370,
            triggerRange        = 1000,
            actorX              = 35820,
            actorZ              = -1950,
            actorY              = 46370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1CE
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1DA'),
        (-1, 'loc_1EC'),
    )

    def _loc_1DA(): pass

    label('loc_1DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 0, 0x408)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E9',
    )

    SetScenaFlags(ScenaFlag(0x0081, 0, 0x408))
    Event(0, 0x0003)

    def _loc_1E9(): pass

    label('loc_1E9')

    Jump('loc_1EC')

    def _loc_1EC(): pass

    label('loc_1EC')

    Return()

# id: 0x0001 offset: 0x1ED
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -101000, -72000, 196651)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 7, 0x4B7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_211',
    )

    OP_6F(0x0000, 0)

    Jump('loc_218')

    def _loc_211(): pass

    label('loc_211')

    OP_6F(0x0000, 60)

    def _loc_218(): pass

    label('loc_218')

    PlaySE(452, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x21E
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_233',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_233(): pass

    label('loc_233')

    Return()

# id: 0x0003 offset: 0x234
@scena.Code('func_03_234')
def func_03_234():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetChrPos(0x0101, 86290, -1980, 133350, 270)
    SetChrPos(0x0102, 86870, -1900, 132340, 270)
    CameraMove(86290, -1980, 133350, 0)
    OP_6C(45000, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010040366V#004F哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040367V#014F怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, 0x0004)
    CreateThread(0x0102, 0x01, 0x00, 0x0005)

    @scena.Lambda('lambda_02D3')
    def lambda_02D3():
        CameraMove(46610, -2000, 127240, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_02D3)

    @scena.Lambda('lambda_02EB')
    def lambda_02EB():
        OP_67(0, 4170, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_02EB)

    @scena.Lambda('lambda_0303')
    def lambda_0303():
        CameraSetDistance(4270, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0303)

    @scena.Lambda('lambda_0313')
    def lambda_0313():
        OP_6C(249000, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0313)

    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0102, 0x0001)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010040368V#001F快看快看，约修亚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040369V是海啊，大海啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040370V#010F是是。\n',
            '你不说我也看到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040371V#501F碧蓝的海面上闪着波光，\n',
            '大得一望无边啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040372V还有海浪的声音，\n',
            '浪花拍打岸边散发的海水味……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040373V#001F嗯～～这就是大海的感觉呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 300)

    ChrTalk(
        0x0102,
        (
            '#0020040374V#010F艾丝蒂尔，你第一次看见大海吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040375V#000F以前和老爸一起坐定期船的时候，\n',
            '好像曾经看过一眼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040376V不过能在这么近的距离看，\n',
            '还是第一次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040377V#010F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040378V#019F我也很久没有见过大海了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040379V看来我们没坐定期船，\n',
            '特地步行过来真是值得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040380V#001F嗯嗯！\n',
            '我突然觉得很有成就感呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_058D')
    def lambda_058D():
        CameraSetDistance(3200, 1800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_058D)

    @scena.Lambda('lambda_059D')
    def lambda_059D():
        OP_6C(225000, 1800)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_059D)

    @scena.Lambda('lambda_05AD')
    def lambda_05AD():
        OP_67(0, 9500, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_05AD)

    OP_69(0x0000, 2000)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x5C9
@scena.Code('func_04_5C9')
def func_04_5C9():
    Sleep(500)

    ChrWalkTo(0x00FE, 73720, -1980, 133840, 6000, 0x00)
    ChrWalkTo(0x00FE, 51840, -2070, 128210, 6000, 0x00)
    SetChrDirection(0x00FE, 288, 400)

    Return()

# id: 0x0005 offset: 0x5FE
@scena.Code('func_05_5FE')
def func_05_5FE():
    Sleep(500)

    Sleep(500)

    ChrWalkTo(0x00FE, 73720, -1980, 133840, 6000, 0x00)
    ChrWalkTo(0x00FE, 52140, -2000, 127110, 6000, 0x00)
    SetChrDirection(0x00FE, 288, 400)

    Return()

# id: 0x0006 offset: 0x638
@scena.Code('func_06_638')
def func_06_638():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 7, 0x4B7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7E2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 0, 0x4B8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_714',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    SetChrPos(0x0008, 35820, 500, 46370, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_0687')
    def lambda_0687():
        ChrMoveTo(0x00FE, 35820, -1000, 46370, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0687)

    @scena.Lambda('lambda_06A2')
    def lambda_06A2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_06A2)

    ClearChrFlags(0x0008, 0x0080)

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
    Battle(0x00000171, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_6EF'),
        (0x00000002, 'loc_701'),
        (0x00000001, 'loc_711'),
        (-1, 'loc_714'),
    )

    def _loc_6EF(): pass

    label('loc_6EF')

    SetScenaFlags(ScenaFlag(0x0097, 0, 0x4B8))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_714')

    def _loc_701(): pass

    label('loc_701')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_711(): pass

    label('loc_711')

    OP_B4(0x00)

    Return()

    def _loc_714(): pass

    label('loc_714')

    If(
        (
            (Expr.Eval, "AddItem(0x0134, 1)"),
            Expr.Return,
        ),
        'loc_76A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '百合项链',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0096, 7, 0x4B7))

    Jump('loc_7DF')

    def _loc_76A(): pass

    label('loc_76A')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '百合项链',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '百合项链',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_7DF(): pass

    label('loc_7DF')

    Jump('loc_818')

    def _loc_7E2(): pass

    label('loc_7E2')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x82)
    def _loc_818(): pass

    label('loc_818')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
