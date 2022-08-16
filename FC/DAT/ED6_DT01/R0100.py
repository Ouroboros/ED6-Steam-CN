import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R0100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0100   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R0100.x'
    header.mapIndex       = 23
    header.bgm            = 20
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
            dword_00        = 0xFFFF7748,
            dword_04        = 0x000003E8,
            dword_08        = 0x00023280,
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
            word_3A         = 23,
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
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT09/CH10180._CH', 'ED6_DT09/CH10180P._CP'),
        ('ED6_DT09/CH10181._CH', 'ED6_DT09/CH10181P._CP'),
        ('ED6_DT09/CH10260._CH', 'ED6_DT09/CH10260P._CP'),
        ('ED6_DT09/CH10261._CH', 'ED6_DT09/CH10261P._CP'),
        ('ED6_DT09/CH10210._CH', 'ED6_DT09/CH10210P._CP'),
        ('ED6_DT09/CH10211._CH', 'ED6_DT09/CH10211P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '洛连特方向',
            x                   = -14030,
            z                   = 1000,
            y                   = 217340,
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
            name                = '布莱特家方向',
            x                   = -60890,
            z                   = 1030,
            y                   = 216800,
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
            name                = '格鲁纳门方向',
            x                   = -39320,
            z                   = 1000,
            y                   = 90280,
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

# id: 0x10002 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x14A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x14A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -36800,
            triggerZ            = 1000,
            triggerY            = 152300,
            triggerRange        = 1500,
            actorX              = -36800,
            actorZ              = 2500,
            actorY              = 152800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -39100,
            triggerZ            = 1000,
            triggerY            = 153300,
            triggerRange        = 1500,
            actorX              = -39100,
            actorZ              = 2200,
            actorY              = 153300,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x192
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_19E'),
        (-1, 'loc_207'),
    )

    def _loc_19E(): pass

    label('loc_19E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A7',
    )

    Return()

    def _loc_1A7(): pass

    label('loc_1A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0043, 0, 0x218)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_204',
    )

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    CameraMove(-14000, 1000, 197160, 0)
    ChrSetPos(0x0102, -13816, 1000, 198240, 180)
    ChrSetPos(0x0101, -14816, 1000, 199400, 180)
    OP_6C(40000, 0)
    MapSetFlags(0x00400000)
    FadeIn(500, 0)
    Event(0, func_04_2F4)

    def _loc_204(): pass

    label('loc_204')

    Jump('loc_207')

    def _loc_207(): pass

    label('loc_207')

    Return()

# id: 0x0001 offset: 0x208
@scena.Code('func_01_208')
def func_01_208():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_220',
    )

    OP_B1('R0100_y')

    Jump('loc_229')

    def _loc_220(): pass

    label('loc_220')

    OP_B1('R0100_n')

    def _loc_229(): pass

    label('loc_229')

    OP_16(0x02, 4000, -164000, 28000, 196616)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_248',
    )

    OP_1B(0x02, 0x00, 0x0007)

    def _loc_248(): pass

    label('loc_248')

    Return()

# id: 0x0002 offset: 0x249
@scena.Code('func_02_249')
def func_02_249():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　洛连特市　　　４９塞尔矩\n',
            '南　格鲁纳门　　２５９塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0x2B5
@scena.Code('func_03_2B5')
def func_03_2B5():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　布莱特家',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0x2F4
@scena.Code('func_04_2F4')
def func_04_2F4():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    CreateThread(0x0101, 0x00, 0x00, func_05_937)
    CreateThread(0x0102, 0x00, 0x00, func_06_966)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    @scena.Lambda('lambda_0315')
    def lambda_0315():
        CameraMove(-13905, 1000, 185268, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0315)

    OP_A5(0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010001074V#003F对了，约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A5(0x0001)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001075V#010F嗯，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001076V#003F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001077V#003F我……\n',
            '真的适合做游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001078V#010F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001079V#015F嗯，我觉得你从父亲那儿继承来的\n',
            '武术能力有扎实的功底……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001080V#015F遇到有困难的人不会放着不管，\n',
            '这种爱管闲事的性格也是你的优点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001081V#008F嘿嘿，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001082V#010F难道……\n',
            '你还在想刚才塔里那件事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001083V#003F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001084V#003F那时候，因为我的大意，\n',
            '差点把鲁克也牵连进去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001085V#003F如果老爸没来，\n',
            '说不定还会让他受重伤。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001086V#003F这样子下去真的能行吗……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001087V#010F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001088V#019F什么呀，说这种话可不是你的风格哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001089V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001090V#010F今天的失败，\n',
            '就用明天来把它挽回。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001091V#010F顾虑太远的事情而畏缩，\n',
            '这可一点也不像你哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001092V#010F这不是你一直憧憬的工作吗？\n',
            '遇到这点挫折就沮丧怎么能行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001093V#003F约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001094V#500F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001095V#500F……嗯，有道理……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001096V#006F这样子，根本不像我嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001097V#011F对对，\n',
            '凝重的表情不适合艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001098V#011F这种乐天派的笑容才自然嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001099V#009F喂，这话是什么意思啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001100V#009F真是的，多此一句……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001101V#019F哈哈，听出来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001102V#000F算了……\n',
            '谢谢，现在我心情好多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001103V#001F那么，赶快回家吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001104V#001F不知为什么突然就觉得肚子饿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001105V#010F（果然是乐天派……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    SetScenaFlags(ScenaFlag(0x0043, 0, 0x218))
    MapClearFlags(0x00400000)
    EventEnd(0x00)
    MapSetFlags(0x00000001)

    Return()

# id: 0x0005 offset: 0x937
@scena.Code('func_05_937')
def func_05_937():
    OP_A6(0x0000)
    ChrWalkTo(0x00FE, -14551, 0, 186301, 3000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    OP_92(0x00FE, 0x0000, 0, 3000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0006 offset: 0x966
@scena.Code('func_06_966')
def func_06_966():
    OP_A6(0x0001)
    ChrWalkTo(0x00FE, -13516, 0, 184435, 3000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    OP_92(0x00FE, 0x0000, 0, 3000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0007 offset: 0x995
@scena.Code('func_07_995')
def func_07_995():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B5E',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_A37',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001071V#010F已经傍晚了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001072V#010F父亲还在等我们呢，\n',
            '我们还是早点回家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001073V#000F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B43')

    def _loc_A37(): pass

    label('loc_A37')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AEF',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020000218V#014F艾丝蒂尔，去城里不是这个方向啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000219V你该不会还没有睡醒吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000220V#009F真、真啰嗦啊你～\n',
            '刚才只不过看错路牌而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B43')

    def _loc_AEF(): pass

    label('loc_AEF')

    ChrTalk(
        0x0102,
        (
            '#0020000221V#012F（这方向是往王都地区的……\n',
            '　要去城里的话往反方向走就行了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B43(): pass

    label('loc_B43')

    ChrMoveToRelative(0x0000, 0, 0, 2500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_B5E(): pass

    label('loc_B5E')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
